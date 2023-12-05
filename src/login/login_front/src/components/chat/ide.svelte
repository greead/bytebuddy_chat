<script lang="ts">
    import * as ace from 'brace'
    import 'brace/mode/javascript'
    import "brace/mode/python";
    import "brace/theme/tomorrow_night_bright";
    import 'brace/theme/monokai'
    import "brace/ext/searchbox";
    import "brace/snippets/python"
    import "brace/ext/language_tools"
    import { ide_contents, wss_ide, username, ide_state } from "../store"
    import { onDestroy, onMount } from "svelte";

    let editor: ace.Editor;

    onMount(() => {
        editor = ace.edit('editor');
        let options = {"fontSize":16, "scrollPastEnd":true, enableBasicAutocompletion: true, enableSnippets: true, enableLiveAutocompletion: true,}
        editor.getSession().setMode('ace/mode/python')
        editor.setTheme('ace/theme/tomorrow_night_bright')
        editor.setOptions(options)
        editor.on('change', onChangeHandler)
        // editor.on('change', onChangeHandler)
        editor.$blockScrolling = Infinity

        ide_contents.subscribe((delta) => {
            if(delta) {
                console.log('FROM SUB', delta)
                if (delta.user != $username) {
                    editor.off('change', onChangeHandler)
                    editor.getSession().getDocument().applyDeltas([delta])
                    editor.on('change', onChangeHandler)
                }                
                
            } 
        })

        ide_state.subscribe((state) => {
            editor.off('change', onChangeHandler)
            editor.setValue(state)
            editor.on('change', onChangeHandler)
        })
    })



    function onChangeHandler(event) {
        $wss_ide.sendMessage({...event, user:$username, current_state:editor.getValue()})
        console.log("CHANGE", event)        
    }

    onDestroy(() => {
        $wss_ide.disconnectWebSocket()
    })


    
</script>

<div id="editor"></div>

<style>
  #editor {
    padding: 1em;
    background-color: black;
    border: 1em solid black;
    height: 40vh;
  }
</style>