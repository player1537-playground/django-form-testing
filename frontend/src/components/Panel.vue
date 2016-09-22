<template>
  <div class="panel panel-default">
    <label class="panel-heading" style="width:100%" v-show="hasHeading">
      <div class="clearfix">
        <h3 class="panel-title pull-left" >
          <slot name="title" ></slot>
        </h3>
        <div class="btn-group pull-right">
          <button type="button"  class="btn btn-xs" @click.stop.prevent="pressed">
            <span class="glyphicon glyphicon-minus"></span>
          </button>
        </div>
      </div>
    </label>
    <div class="panel-collapse collapse" :class="{ 'in': expanded }">
      <div class="panel-body" >
        <slot></slot>
      </div>
    </div>
    <div class="panel-footer" v-show="hasFooter" >
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Panel',
  props: {
    expanded: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    hasHeading() {
      return typeof this._slotContents.title !== 'undefined';
    },
    hasFooter() {
      return typeof this._slotContents.footer !== 'undefined';
    },
  },
  methods: {
    pressed(e) {
      this.$emit('change', { target: { value: { expanded: !this.expanded } } });
    },
  },
};
</script>
