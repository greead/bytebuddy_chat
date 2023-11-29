<script>
    import { uri, wss, current_room } from "../store";
    import { get } from "svelte/store";

    export let roomName = "Room";

    async function connectRoom() {
        if (get($wss).isConnected){
            $wss.disconnectWebSocket()
        }

        uri.set(`ws://localhost:8000/ws/chat/${roomName.replaceAll(' ', '')}/`)
        current_room.set(`${roomName}`)
        $wss.connectWebSocket()
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