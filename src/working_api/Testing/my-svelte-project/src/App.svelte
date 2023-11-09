<script>
  import Csrf from "../components/csrf.svelte";
  import Login from "../components/login.svelte";
    import Logout from "../components/logout.svelte";
  import Session from "../components/session.svelte";
  import {auth, csrf, username, password, data, sessionid, page} from "../components/store"

</script>

<Csrf/>
<p>{$csrf}</p>

<Session/>
<p>{$auth}</p>
<p>{$sessionid}</p>

<Login/>
<p>{$username}</p>
<p>{$password}</p>

<Logout/>

<p>{$data}</p>

{#if $page == 'login'}
<Login/>
<p>{$username}</p>
<p>{$password}</p>
{:else if $page == 'logout'}
<Logout/>
{/if}