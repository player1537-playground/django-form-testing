<template>
  <div>
    <div class="col-xs-9">
      <panel>
        <span slot="title">Reduction</span>
        <div class="form-group">
          <div class="form-group">
            <label for="reduction-route-title">Title</label>
            <input type="text" id="reduction-route-title" class="form-control" placeholder="title"/>
          </div>

          <div class="form-group">
            <label for="reduction-route-ipts">IPTS</label>
            <input type="text" id="reduction-route-ipts" class="form-control" placeholder="ipts"/>
          </div>

          <div class="form-group">
            <label for="reduction-route-configuration">Configuration</label>
            <input type="text" id="reduction-route-configuration" class="form-control" placeholder="configuration"/>
          </div>

        </div>

        <ul role="tablist" class="nav nav-tabs" style="margin-bottom:15px">
          <li v-for="tab in tabs" role="presentation" :class="{ 'dropdown': tab.active, 'active': tab.active }">
            <a v-if="!tab.active" role="tab" v-link="{ name: 'reduction' }" @click.stop.prevent="setActiveTab(tab)">
              {{ tab.name }}
            </a>
            <input v-if="tab.active && tab.editing" v-focus-auto v-model="renameText" type="text" @keyup.enter.stop.prevent="finishRenamingTab(tab)" v-on-clickaway="finishRenamingTab(tab)">
            <a v-if="tab.active && !tab.editing" role="button" v-link="{ name: 'reduction' }" data-toggle="dropdown" class="dropdown-toggle">
              <span>{{ tab.name }}</span><span class="caret"></span>
            </a>
            <ul v-if="tab.active && !tab.editing" class="dropdown-menu">
              <li><a href="#" @click.stop.prevent="deleteTab(tab)">Delete</a></li>
              <li>
                <a href="#" @click.stop.prevent="startRenamingTab(tab)">Rename</a>
              </li>

            </ul>

          </li>
          <li role="presentation">
            <a href="" role="tab" v-link="{ name: 'reduction' }" @click="addNewTab"><span class="glyphicon glyphicon-plus"></span></a>
          </li>
        </ul>

        <div class="tab-content">

          <div class="form-group">
            <label for="reduction-route-beam-center">Beam Center</label>
            <input type="text" id="reduction-route-beam-center" class="form-control" placeholder="beam center"/>
          </div>

          <div role="tabpanel" class="tab-pane active" role="tabpanel">
            <handsontable :data="activeTab.data" :settings="tableOptions"></handsontable>
          </div>
        </div>
      </panel>
    </div>
  </div>
</template>

<script>
import Panel from './Panel.vue';
import SidebarPanel from './SidebarPanel.vue';
import Handsontable from './Handsontable.vue';
import { focusAuto } from 'vue-focus';
import { directive as onClickaway } from 'vue-clickaway';

export default {
  name: 'ReductionRoute',
  directives: {
    focusAuto,
    onClickaway,
  },
  components: {
    SidebarPanel,
    Panel,
    Handsontable,
  },
  data() {
    return {
      renameText: '',
      tabs: [
        { name: 'Low', active: true, editing: false, data: [] },
        { name: 'Med', active: false, editing: false, data: [] },
        { name: 'High', active: false, editing: false, data: [] },
      ],
      tableOptions: {
        minSpareRows: 10,
        className: 'htCenter',
        rowHeaders: true,
        colHeaders: ['Name', 'Sample Scattering', 'Sample Transmission', 'Background Scattering', 'Background Transmission'],
        columns: [
          {},
          {},
          {},
          {},
          {},
        ],
        height: 500,
        stretchH: 'all',
      },
    };
  },

  computed: {
    activeTab() {
      return this.tabs.find(d => d.active);
    },
  },

  methods: {
    setActiveTab(tab) {
      this.activeTab.active = false;
      tab.active = true;
    },

    addNewTab() {
      var newTab = {
        name: 'Tab ' + this.tabs.length,
        active: false,
        data: [],
      };

      console.log(this.tabs);
      this.tabs.push(newTab);
      console.log(this.tabs);
      this.setActiveTab(newTab);
    },

    startRenamingTab(tab) {
      this.renameText = tab.name;
      tab.editing = true;
    },

    finishRenamingTab(tab) {
      tab.editing = false;
      tab.name = this.renameText;
    },

    deleteTab(tab) {
      var index = this.tabs.findIndex(d => d === tab);

      this.tabs.splice(index, 1);

      if (this.tabs.length > 0) {
        this.tabs[0].active = true;
      }
    },
  },
};
</script>
