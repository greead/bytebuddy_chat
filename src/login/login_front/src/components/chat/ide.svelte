<script>
// @ts-nocheck

    import { AceEditor } from "svelte-ace";
    import "brace"
    import "brace/mode/python";
    import "brace/theme/tomorrow_night_bright";
    import "brace/ext/searchbox";
    import "brace/snippets/python"
    import "brace/ext/language_tools"
    import { ide_contents, wss_ide, isUnchanged } from "../store"
    import { onDestroy, onMount } from "svelte";

    function updateIde(obj) {
        $wss_ide.sendMessage(obj.detail)
        // console.log(obj.detail)
    }

    onDestroy(() => {
        $wss_ide.disconnectWebSocket()
    })


    let options = {"fontSize":16, "scrollPastEnd":true, enableBasicAutocompletion: true, enableSnippets: true, enableLiveAutocompletion: true,}
</script>

<div class="editor">
    <AceEditor width='100%' height='300px' lang="python" theme="tomorrow_night_bright" value={$ide_contents} {options} on:documentChange={updateIde}/>
</div>


<style>
    .editor {
        padding: 1em;
        background-color: black;
    }
    
</style>