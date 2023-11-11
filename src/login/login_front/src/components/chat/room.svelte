<script>
    import { uri, wss } from "../store";

    export let roomName = "Room";

    async function connectRoom() {
        uri.set('wss://socketsbay.com/wss/v2/1/demo/')
        $wss.connectWebSocket()
    }

</script>

<div>
    <button on:click={connectRoom} >{roomName}</button>
</div>

<style>
    div {
        display: grid;
    }
</style>