<script>
  /**
   * Main svelte component for the login app
   * Responsible for showing and swapping between different user/auth pages
   * Pages: Signup, Login
  */
  import {Router, Route, Link} from 'svelte-routing';
  import Signup from "./components/signup.svelte";
  import Login from "./components/login.svelte";
  import Logout from "./components/logout.svelte"
  import Landing from "./components/landing.svelte"
  import ChatApp from './components/chat_app.svelte';
  export let url="";
</script>

<svelte:head>
  <link href="https://fonts.googleapis.com/css?family=VT323" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Rubik+Pixels" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/y-grid" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/phatone" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/mastodontus" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/zuber-future" rel="stylesheet">          
</svelte:head>

<Router {url}>
  <!-- <nav>
    <Link to="/">Login</Link>
    <Link to="/signup">Signup</Link>
  </nav> -->
    <Route path="/" component={Landing} />
    <Route path="/signup/" component={Signup} />
    <Route path="/login/" component={Login} />
    <Route path="/logout" component={Logout} />
    <Route path="/chat/" component={ChatApp} />
</Router>
