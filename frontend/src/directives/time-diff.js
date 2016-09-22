import moment from 'moment';

export default {
    update(newValue, oldValue) {
        var value = null;
        if (typeof newValue.length === 'undefined') {
            value = moment.duration(newValue, 'seconds').humanize();
        } else {
            var start = moment(newValue[0]),
                end = moment(newValue[1]);

            value = end.diff(start);
        }

        this.el.innerText = value;
    },
};
