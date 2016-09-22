<template>
  <div class="handsontable" v-el:table></div>
</template>

<script>
import Handsontable from 'handsontable/dist/handsontable.full.js';

export default {
  name: 'Handsontable',
  props: {
    data: {
      type: Array,
      required: true,
      default() { return []; },
    },
    settings: {
      type: Object,
      required: false,
      default() { return {}; },
    },
  },

  data() {
    return { table: null };
  },

  computed: {
    fullSettings() {
      return Object.assign({}, this.settings, { data: this.data });
    },
  },

  watch: {
    fullSettings() {
      if (this.table !== null) {
        this.table.loadData(this.fullSettings.data);
      }
    },
  },

  ready() {
    console.log('Creating handsontable');
    this.table = new Handsontable(this.$els.table, this.fullSettings);
  },

  beforeDestroy() {
    if (this.table !== null) {
      this.table.destroy();
    }
    this.table = null;
  },
};
</script>

<style>
@import '~handsontable/dist/handsontable.full.css';
</style>
