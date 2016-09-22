<template>
    <div class="col-xs-6 col-xs-offset-3">
        <panel>
            <span slot="title">Login</span>
            <form>
                <div class="form-group" >
                    <label for="loginUsername" >Username</label>
                    <input type="text" class="form-control" id="loginUsername"  placeholder="Username">
                </div>
                <div class="form-group" >
                    <label for="loginPassword" >Password</label>
                    <input type="password" class="form-control" id="loginPassword"  placeholder="Password">
                </div>
                <button type="submit" class="btn btn-default" @click.stop.prevent="">Submit</button>

            </form>
        </panel>
    </div>
</template>

<script>
import Panel from './Panel.vue';

export default {
    name: 'LoginRoute',
    components: {
        Panel,
    },
};
</script>
