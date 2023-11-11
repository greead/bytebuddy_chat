<script>
    import Logout from "../auth/logout.svelte";
    import Chatbox from "./chatbox.svelte";
    import RoomsBar from "./rooms_bar.svelte";
    import Ide from "./ide.svelte";
    import UsersBar from "./users_bar.svelte";


</script>

<div class="topbar">
    <Logout/>
</div>


<div class="chatbox">
    <div class="main">
        <RoomsBar/>
        <div>
            <Ide/>
            <Chatbox/>
        </div>
        <UsersBar/>
    </div>

</div>


<style>
    .chatbox {
        width: max-content;
    }
    .main {
        display: flex;
        align-items: start;
    }
    .topbar {
        margin-left: auto;
        margin-right: 0;
    }
</style>

