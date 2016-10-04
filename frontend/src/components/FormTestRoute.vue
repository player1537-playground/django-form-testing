<template>
  <div>
    <div class="col-xs-9">
      <panel>
        <span slot="title">FormTest</span>
        <template v-if="schema">
          <vue-form-generator :schema="schema"
                              :model="model">
          </vue-form-generator>
          <button type="submit"
                  class="btn btn-primary pull-right">
            Submit
          </button>
        </template>
      </panel>
    </div>
  </div>
</template>

<script>
import Panel from './Panel.vue';
import { component as VueFormGenerator } from 'vue-form-generator';
import resource from '../resource';

export default {
  name: 'FormTestRoute',

  components: {
    Panel,
    VueFormGenerator,
  },

  route: {
    data({ next, abort }) {
      resource.posts.schema.get().then((response) => {
        next(response.json());
      }).catch((response) => {
        abort(response.json());
      });
    },
  },

  data() {
    return {
      schema: null,
      model: {
        title: '',
        content: '',
        published: false,
        tag: '',
      },
    };
  },

};
</script>
