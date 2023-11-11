<script>
    import Logout from "../auth/logout.svelte";
    import Chatbox from "./chatbox.svelte";
    import RoomsBar from "./rooms_bar.svelte";
    import Ide from "./ide.svelte";
    import UsersBar from "./users_bar.svelte";
    import { onMount } from "svelte";

    let roomsList = []
    let profilesList = []

    onMount(() => {
        getRoomsList()
        getProfilesList()
    })

    async function getRoomsList() {
        let apiRooms = []
        // TODO fetch rooms from API
        roomsList = ["Dummy1", "Dummy2", "Dummy 3"] // <-- Placeholder
    }

    async function getProfilesList() {
        let apiProfiles = []
        // TODO fetch profiles from API
        profilesList = ["User 1", "User 2", "User 3"] // <-- Placeholder
    }

</script>

<div class="system">
    <div class="topbar">
        <button>Profile</button>
        <Logout/>
    </div>
    
    
    <div class="chatbox">
        <div class="main">
            <RoomsBar rooms={roomsList}/>
            <div>
                <Ide/>
                <Chatbox/>
            </div>
            <UsersBar users={profilesList}/>
        </div>
    
    </div>
</div>



<style>
    .main {
        display: flex;
        align-items: start;
    }
    .topbar {
        padding-bottom: 15px;
    }
</style>

