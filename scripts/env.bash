#!/bin/bash

env-line-without-value() {
    local line var value
    line=$1

    if [ "${#line}" -eq 0 ] || [ "${line:0:1}" = "#" ]; then
        printf '%s\n' "$line"
        return
    fi

    var=${line%%=*};
    value=${line#*=};
    printf '%s\n' "$var";
}

env-without-values() {
    local filename var value
    filename=$1

    while IFS= read -r line || [[ -n "$line" ]]; do
        env-line-without-value "$line"
    done < "$filename"
}

env-variables() {
    local filename var value
    filename=${1:-.env}

    while IFS= read -r line || [[ -n "$line" ]]; do
        if [ "${#line}" -eq 0 ] || [ "${line:0:1}" = "#" ]; then
            continue
        fi

        var=${line%%=*};
        value=${line#*=};
        printf '%s\n' "$var";
    done < "$filename"
}

env-diff() {
    local cur base columns ret
    cur=${1:-.env}
    base=${2:-.env.base}
    columns=${COLUMNS:-$(tput cols)}

    if diff -q <(env-without-values $cur) <(env-without-values $base); then
        return 0
    fi

    diff --side-by-side -W "$columns" \
         <(env-without-values $cur) \
         <(env-without-values $base)
    ret=$?

    fold -w "$columns" -s <<EOF

On the left is the current set of variables as defined in your current settings, and on the right is the set of variables in the .env.base file.

Lines with a ">" between them are ones that you should add to your current .env file, and lines with a "<" are those which have been deprecated.

EOF

    return $ret
}

env-to-makefile() {
    local env_file sep
    env_file=${1:-.env}

    printf 'ENV_VARIABLES :=\n'

    while IFS= read -r line || [[ -n "$line" ]]; do
        [ "${#line}" -eq 0 ] && continue;
        [ "${line:0:1}" = "#" ] && continue;
        var=${line%%=*};
        value=${line#*=};
        printf 'define %s\n' "$var"
        printf '%s\n' "$value"
        printf 'endef\n'
        printf 'export %s\n' "$var"
        printf 'ENV_VARIABLES := $(ENV_VARIABLES) %s\n' "${var:+$var }"
        printf '\n'
    done <"$env_file"
}

env-merge() {
    local current_file base_file old_ifs current_parsed base_parsed
    current_file=${1:-.env}
    base_file=${2:-.env.base}
    old_ifs=$IFS
    IFS=

    while true; do
        if ! read -r current || [[ -n "$current" ]]; then
            cat <&3
        fi
        while true; do
            read -r base <&3 || [[ -n "$base" ]] || break 2
            current_parsed=$(env-line-without-value "$current")
            base_parsed=$(env-line-without-value "$base")
            if [[ $current_parsed == $base_parsed ]]; then
                printf '%s\n' "$current"
                break
            else
                printf '%s\n' "$base"
            fi
        done
    done <"$current_file" 3<"$base_file"

    IFS=$old_ifs
}

env-subst() {
    local filename variables i formatted oifs
    filename=${1:-.env}

    oifs=$IFS
    IFS=$'\n'

    variables=( PWD $(env-variables "$filename") )
    for ((i=0; i<${#variables[@]}; ++i)); do
        variables[$i]=\$${variables[$i]}
    done

    IFS=,
    formatted="${variables[*]}"

    IFS=$oifs

    set -o allexport
    source "$filename"
    set +o allexport
    exec envsubst "$formatted"
}

env-main() {
    local action
    action=$1; shift

    case "$action" in
        (diff) env-diff "$@";;
        (to-makefile) env-to-makefile "$@";;
        (merge) env-merge "$@";;
        (subst) env-subst "$@";;
        (variables) env-variables "$@";;
        (*) printf $'Unknown action: "%s"\n' "$action"; exit 1;;
    esac
}

env-main "$@"
