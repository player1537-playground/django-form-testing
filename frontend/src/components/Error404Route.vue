<template>
    <div class="col-xs-6 col-xs-offset-3">
        <panel>
            <span slot="title">Error: 404</span>
            <p>Page {{ '/' + ($route.params.source || $route.source) }} could not be found.</p>
        </panel>
    </div>
</template>

<script>
import Panel from './Panel.vue';

export default {
    name: 'Error404Route',
    components: {
        Panel,
    },
};
</script>
