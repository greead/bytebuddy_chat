<script>
    import Logout from "./logout.svelte";
    import Chatbox from "./chatbox.svelte";
    import RoomsBar from "./rooms_bar.svelte";
    import Ide from "./ide.svelte";
    import UsersBar from "./users_bar.svelte";
</script>

<div class="chatbox">
    <div class="main">
        <RoomsBar/>
        <div>
            <Ide/>
            <Chatbox/>
        </div>
        <UsersBar/>
    </div>
    <br><br>
    <Logout/>
</div>


<style>
    .chatbox {
        width: max-content;
    }
    .main {
        display: flex;
        align-items: start;
    }
</style>

