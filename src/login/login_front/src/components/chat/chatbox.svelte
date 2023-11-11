<script>
    import { onDestroy, onMount } from "svelte";
    import { uri, wss } from "../store";

    let messageList = []
    let inputMessage = ""

    onMount(() => {
        loadMessages()
    })

    onDestroy(() => {
        $wss.disconnectWebSocket()
    })

    $wss.subscribe((store) => {
        messageList = [...messageList, store.message]
    })

    async function handleMessage(event) {
        $wss.sendMessage(inputMessage)
    }

    async function loadMessages() {
        let apiMessages = []
        // TODO Fetch messages from api
        messageList = [apiMessages, ...messageList] // <-- Not a placeholder, don't change
    }

</script>

<div class="chatbox">
    <div id="messageArea" class="messageArea">        
        <ul role="listbox">
            {#each messageList as message, i}
                <li>{message}</li>
            {/each}
        </ul>
    </div>
    
    <div id="messageBox" class="messageBox">
        <input bind:value={inputMessage} type="text" id="textBox" name="textBox" class="textBox">
        <button on:click={handleMessage} class="submit">Send</button>
    </div>
</div>


<style>
    ul {
        list-style: none;
        margin: 0;
        padding: 0;
        text-align: left;
        max-height: 20vh;
        text-indent: 10px;
        overflow: auto;
    }
    .messageArea {
        width: 100%;
        height: 20vh;
        border: 1px solid #333;
        padding: 0;
        background-color: white;
        
    }
    .messageBox {
        display: flex;
        width: 50vw;
        height: fit-content;
        margin-top: 4px;
    }
    .textBox {
        height: 2em;
        padding: 0;
        margin: 0;
        width: 80%;
    }
    .submit {
        padding: 0;
        margin: 0;
        width: 20%;
        border-radius: 0;
    }
    .chatbox {
        width: 50vw;
    }
</style>