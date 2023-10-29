<script>
  /**
   * Main svelte component for the login app
   * Responsible for showing and swapping between different user/auth pages
   * Pages: Signup, Login
  */
  import Signup from "./components/signup.svelte";
</script>

<main>
  <Signup/>
</main>

<style>
  /* 
  Styles commented out for potential future use 

  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  } */
</style>
