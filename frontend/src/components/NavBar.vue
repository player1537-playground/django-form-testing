<template>
  <nav class="navbar navbar-default navbar-fixed-top">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" v-link="{ name: 'default' }"><img src="../assets/logo.png" alt="Dispute Bills"></a>
      </div>
      <div id="navbar" class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
          <nav-item name="catalog"><span class="glyphicon glyphicon-book"></span> &nbsp;Catalog</nav-item>
          <li class="dropdown dropdown-hover" >
            <a href="#" class="dropdown-toggle" data-toggle="dropdown"  role="button" ><span class="glyphicon glyphicon-th-list"></span> &nbsp;Configuration <span class="caret"></span></a>
            <ul class="dropdown-menu" >
              <nav-item name="">New</nav-item>
              <nav-item name="">List</nav-item>
            </ul>
          </li>
          <li class="dropdown dropdown-hover" >
            <a href="#" class="dropdown-toggle" data-toggle="dropdown"  role="button" ><span class="glyphicon glyphicon-th"></span> &nbsp;Reduction <span class="caret"></span></a>
            <ul class="dropdown-menu" >
              <nav-item name="reduction">New</nav-item>
              <nav-item name="">List</nav-item>
            </ul>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li class="dropdown dropdown-hover" >
            <a href="#" class="dropdown-toggle" data-toggle="dropdown"  role="button" ><span class="glyphicon glyphicon-user"></span> &nbsp; Dev <span class="caret"></span></a>
            <ul class="dropdown-menu" >
              <nav-item name="login">Login</nav-item>
              <nav-item name="profile">Profile</nav-item>
              <nav-item name="form-test">FormTest</nav-item>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style>

.navbar-brand {
  padding: 0px;
}

.navbar-brand>img {
  width: auto;
  display: inline-block;
  height: 50px;
  margin-top: -12px
}

.dropdown:hover .dropdown-menu {
display: block;
}

</style>

<script>
import NavItem from './NavItem.vue';
export default {
  name: 'NavBar',
  components: {
    NavItem,
  },
};
</script>
