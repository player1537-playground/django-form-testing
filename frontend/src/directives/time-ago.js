import moment from 'moment';

export default {
    bind() {
        this.$timeAgoTimeout = null;
        this.update();
    },
    update(newValue, oldValue) {
        if (this.$timeAgoTimeout !== null) {
            clearTimeout(this.$timeAgoTimeout);
        }

        var time = moment(newValue);

        this.el.innerText = time.fromNow();
        this.el.title = time.format();

        this.$timeAgoTimeout = setTimeout(() => {
            this.$timeAgoTimeout = null;
            this.update(newValue);
        }, 60*1000);
    },
    unbind() {
        clearTimeout(this.$timeAgoTimeout);
    },
};
