<script>
  /**
   * Main svelte component for the login app
   * Responsible for showing and swapping between different user/auth pages
   * Pages: Signup, Login
  */
  import {Router, Route} from 'svelte-routing';
  import Signup from "./components/auth/signup.svelte";
  import Login from "./components/auth/login.svelte";
  import Logout from "./components/auth/logout.svelte"
  import Landing from "./components/auth/landing.svelte"
  import ChatApp from './components/chat/chat_app.svelte';
  import Profile from "./components/profile/profile.svelte"
  export let url="";
</script>

<!-- Imported stylesheets -->
<svelte:head>
  <link href="https://fonts.googleapis.com/css?family=VT323" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Rubik+Pixels" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/y-grid" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/phatone" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/mastodontus" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/zuber-future" rel="stylesheet"> 
</svelte:head>

<!-- Routing setup -->
<Router {url}>
    <Route path="/" component={Landing} />
    <Route path="/signup/" component={Signup} />
    <Route path="/login/" component={Login} />
    <Route path="/logout" component={Logout} />
    <Route path="/chat/" component={ChatApp} />
    <Route path="/profile/" component={Profile} />
</Router>
