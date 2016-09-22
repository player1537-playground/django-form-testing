<template>
  <li v-link-active>
    <a v-link="route">
      <slot></slot>
    </a>
  </li>
</template>

<script>
export default {
  name: 'NavItem',
  props: {
    name: String,
    params: Object,
  },
  computed: {
    route() {
      var ret = { name: this.name, activeClass: 'active' };
      if (typeof this.params !== undefined) {
        ret.params = this.params;
      }
      return ret;
    },
  },
};
</script>
