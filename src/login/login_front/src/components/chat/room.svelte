<script>
    import { onMount } from "svelte";
    import { uri, uri_ide, wss_ide, wss, current_room, message_list, ide_contents, ide_state } from "../store";
    import { get } from "svelte/store";

    export let roomName = "Room";

    onMount(() => {
        if (roomName === "Home") {
            connectRoom()
        }
    })

    async function connectRoom() {
        message_list.set([])
        ide_state.set('')

        if (get($wss).isConnected){
            $wss.disconnectWebSocket()
        }

        if (get($wss_ide).isConnected){
            $wss_ide.disconnectWebSocket()
        }

        uri.set(`ws://localhost:8000/ws/chat/${roomName.replaceAll(' ', '')}/`)
        uri_ide.set(`ws://localhost:8000/ws/ide/${roomName.replaceAll(' ', '')}/`)

        current_room.set(`${roomName}`)
        
        $wss.connectWebSocket()
        $wss_ide.connectWebSocket()
    }

</script>

<div>
    <button on:click={connectRoom}>{roomName}</button>
</div>

<style>
    div {
        display: grid;
        padding-top: 0.5em;
        padding-bottom: 0.5em;
    }
</style>