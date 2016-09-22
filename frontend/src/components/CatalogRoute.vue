<template>
  <div class="container">
    <div class="row">
      <div class="col-xs-9">
        <panel :expanded="!selectedFacility" @change="selectFacility(null)">
          <span slot="title">Select a Facility {{ selectedFacility ? '(' + selectedFacility.name + ')' : '' }}</span>
          <div v-show="!$loadingRouteData">
            <table class="table table-hover">
              <thead>
                <th>Name</th>
                <th>Description</th>
              </thead>
              <tbody>
                <tr v-for="facility in results" @click.stop.prevent="selectFacility(facility)">
                  <td>{{ facility.name }}</td>
                  <td>{{ facility.desc }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </panel>

        <panel v-if="selectedFacility" :expanded="!selectedInstrument" @change="selectInstrument(null)">
          <span slot="title">Select an Instrument {{ selectedInstrument ? '(' + selectedInstrument.name + ')' : '' }}</span>
          <div>
            <table class="table table-hover">
              <thead>
                <th>Name</th>
                <th>Description</th>
              </thead>
              <tbody>
                <tr v-for="instrument in selectedFacility.instruments" @click="selectInstrument(instrument)">
                  <td>{{ instrument.name }}</td>
                  <td>{{ instrument.desc }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </panel>

        <panel v-if="selectedInstrument" :expanded="!selectedConfiguration" @change="selectConfiguration(null)">
          <span slot="title">Select a Configuration {{ selectedConfiguration ? '(' + selectedConfiguration.name + ')' : '' }}</span>
          <div>
            <table class="table table-hover">
              <thead>
                <th>Name</th>
                <th>Description</th>
              </thead>
              <tbody>
                <tr v-for="configuration in selectedInstrument.configurations" @click="selectConfiguration(configuration)">
                  <td>{{ configuration.name }}</td>
                  <td>{{ configuration.desc }}</td>
                </tr>
                <tr>
                  <td>
                    <input class="form-control" type="text">
                  </td>
                  <td>
                    <div class="row">
                      <div class="col-xs-12">
                        <div class="input-group">
                          <input name="" type="text" value="" class="form-control"/>
                          <span class="input-group-btn"><button class="btn btn-default" type="button">Create</button></span>
                        </div>
                      </div>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </panel>

        <panel v-if="selectedConfiguration">
          <span slot="title">Modify the Configuration</span>
          <div>
            <form class="form-horizontal" action="">
              <div class="form-group" v-for="entry in sortedEntries">
                <label class="col-xs-3 control-label" :for="'entry' + $index">{{ entry.name }}</label>
                <div class="col-xs-9">
                  <input :id="'entry' + $index" class="form-control" type="text" :value="entry.value" :readonly="!advanced && entry.advanced" />
                </div>
              </div>
              <div class="form-group">
                <div class="col-xs-offset-3 col-xs-9">
                  <div class="checkbox">
                    <label>
                      <input type="checkbox" v-model="advanced">Enable Advanced Options</input></label>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </panel>

      </div>
      <div class="col-xs-3">
        <panel>
          <span slot="title">Breadcrumbs</span>
        </panel>
      </div>
    </div>
  </div>
</template>

<script>
import { facility } from '../resource';
import Panel from './Panel.vue';

export default {
  name: 'FacilityRoute',
  data() {
    return {
      count: null,
      next: null,
      previous: null,
      results: null,
      selectedFacility: null,
      selectedInstrument: null,
      selectedConfiguration: null,
      advanced: false,
    };
  },
  computed: {
    sortedEntries() {
      var entries = this.selectedConfiguration.entries.slice();
      entries.sort((a, b) => !!a.advanced - !!b.advanced);
      return entries;
    },
  },
  methods: {
    selectFacility(facility) {
      this.selectInstrument(null);

      if (!facility) {
        this.selectedFacility = null;
        return;
      }

      this.$http.get(facility.url).then(response => {
        this.selectedFacility = response.json();
      });
    },

    selectInstrument(instrument) {
      this.selectConfiguration(null);

      if (!instrument) {
        this.selectedInstrument = null;
        return;
      }

      this.$http.get(instrument.url).then(response => {
        this.selectedInstrument = response.json();
      });
    },

    selectConfiguration(configuration) {
      if (!configuration) {
        this.selectedConfiguration = null;
        return;
      }

      this.$http.get(configuration.url).then(response => {
        this.selectedConfiguration = response.json();
      });
    },

  },
  route: {
    data({ next }) {
      facility.get().then(response => {
        next(response.json());
      });
    },
  },
  components: {
    Panel,
  },
};
</script>
