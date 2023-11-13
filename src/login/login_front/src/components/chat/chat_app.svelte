<script>
    import Logout from "../auth/logout.svelte";
    import Chatbox from "./chatbox.svelte";
    import RoomsBar from "./rooms_bar.svelte";
    import Ide from "./ide.svelte";
    import UsersBar from "./users_bar.svelte";
    import { onMount } from "svelte";
    import Nav from "../navbar/nav.svelte"
    import {userid} from "../store";
    let roomsList = []
    let profilesList = []
    console.log($userid)
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
    <Nav/>
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
    .system{
        display:flex;
        flex-direction: column;
        align-items: center;

    }
    .main {
        display: flex;
        align-items: start;
    }
   
</style>

