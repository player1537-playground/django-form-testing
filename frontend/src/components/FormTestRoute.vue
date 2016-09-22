<template>
  <div>
    <div class="col-xs-9">
      <panel>
        <span slot="title">FormTest</span>
        <vue-form-generator :schema="schema" :model="model"></vue-form-generator>
        <p>name: {{ model.name }}</p>
        <p>email: {{ model.email }}</p>
      </panel>
    </div>
  </div>
</template>

<script>
import Panel from './Panel.vue';
import { component as VueFormGenerator } from 'vue-form-generator';

export default {
  name: 'FormTestRoute',

  components: {
    Panel,
    VueFormGenerator,
  },

  data() {
    return {

      model: {
        name: 'Foo',
        email: 'foo@bar.invalid',
      },

      schema: {
        fields: [

          {
            type: 'text',
            label: 'Your Name',
            model: 'name',
          },

          {
            type: 'email',
            label: 'Your Email',
            model: 'email',
          },

        ],
      }
    };
  },

};
</script>
