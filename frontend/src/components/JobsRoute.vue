<template>
    <div>
        <div class="col-xs-9">
            <panel>
                <span slot="title">Jobs</span>

                <div class="progress">
                    <div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:40%">
                        40% Complete (success)
                    </div>
                </div>
                <div class="progress">
                    <div class="progress-bar progress-bar-info progress-bar-striped" role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100" style="width:50%">
                        50% Complete (info)
                    </div>
                </div>
                <div class="progress">
                    <div class="progress-bar progress-bar-warning progress-bar-striped" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width:60%">
                        60% Complete (warning)
                    </div>
                </div>
                <div class="progress">
                    <div class="progress-bar progress-bar-danger progress-bar-striped" role="progressbar" aria-valuenow="70" aria-valuemin="0" aria-valuemax="100" style="width:70%">
                        70% Complete (danger)
                    </div>
                </div>
                <div class="progress">
                    <div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:40%">
                        40%
                    </div>
                </div>
                <div class="progress">
                    <div class="progress-bar progress-bar-success" role="progressbar" style="width:40%">
                        Free Space
                    </div>
                    <div class="progress-bar progress-bar-warning" role="progressbar" style="width:10%">
                        Warning
                    </div>
                    <div class="progress-bar progress-bar-danger" role="progressbar" style="width:20%">
                        Danger
                    </div>
                </div>
            </panel>
        </div>
        <div class="col-xs-3">
            <sidebar-panel>
                <span slot="title">Remote Jobs</span>
                <div slot="body" class="list-group">
                    <a href="#" class="list-group-item ">see all jobs</a>
                    <a href="#" class="list-group-item active">submit this job</a>
                    <a href="#" class="list-group-item">job 1212</a>
                    <a href="#" class="list-group-item">job 1212</a>
                    <a href="#" class="list-group-item">job 1212</a>
                    <a href="#" class="list-group-item">job 1212</a>
                    <a href="#" class="list-group-item">job 1212</a>
                    <a href="#" class="list-group-item">job 1212</a>
                    <a href="#" class="list-group-item">job 1212</a>
                </div>
            </sidebar-panel>
        </div>
    </div>
</template>

<script>
import Panel from './Panel.vue';
import SidebarPanel from './SidebarPanel.vue';

export default {
    name: 'JobsRoute',
    components: {
        SidebarPanel,
        Panel,
    },
};
</script>
