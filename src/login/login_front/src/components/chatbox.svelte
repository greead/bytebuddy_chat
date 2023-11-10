<script>
    import { onMount } from "svelte";
    // import store from "./store";

    let messageList = []
    let inputMessage = ""
    
    // onMount (() => {
    //     store.subscribe(currentMessage => {
    //         messageList = [...messageList, currentMessage]
    //     })
    // })

    // async function handleMessage(event) {
    //     store.sendMessage(inputMessage)
    //     inputMessage=""
    // }
</script>

<div class="chatbox">
    <div id="messageArea" class="messageArea">
        <div>
            <ul role="listbox">
                {#each messageList as message, i}
                    <li>{message}</li>
                {/each}
            </ul>
        </div>
    </div>
    
    <div id="messageBox" class="messageBox">
        <input bind:value={inputMessage} type="text" id="textBox" name="textBox" class="textBox">
        <!-- <button on:click={handleMessage} class="submit">Send</button> -->
    </div>
</div>


<style>
    ul {
        list-style-type: none;
        margin: 0;
        padding: 0px 8px;
        text-align: left;
    }
    .messageArea {
        width: 100%;
        height: 10em;
        border: 1px solid #333;
        padding: 8px 0px;
        background-color: white;
    }
    .messageBox {
        width: 30em;
        margin-top: 4px;
    }
    .textBox {
        height: 2em;
        width: 79%;
    }
    .submit {
        width: 18%;
    }
</style>