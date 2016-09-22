<template>
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
</template>

<script>

</script>
