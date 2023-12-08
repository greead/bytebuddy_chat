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

    // Set up the Brace editor when the component is mounted.
    onMount(() => {
        editor = ace.edit('editor');
        let options = {"fontSize":16, "scrollPastEnd":true, enableBasicAutocompletion: true, enableSnippets: true, enableLiveAutocompletion: true,}
        editor.getSession().setMode('ace/mode/python')
        editor.setTheme('ace/theme/tomorrow_night_bright')
        editor.setOptions(options)
        editor.on('change', onChangeHandler)
        editor.$blockScrolling = Infinity

        // Subscribe to the ide_contents store (observer).
        // When the IDE contents is updated with a new delta, temporarily
        // deactivate the onChange listeners, apply the deltas, then reactivate the listeners.
        // This should update each time a another user types in the IDE.
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

        // Subscribe to the ide_state store (observer).
        // When the IDE state is updated with a new overall state, temporarily
        // deactivate the onChange listeners, set the contents of the editor, then reactivate
        // the listeners. This should update when a user first connects to the IDE.
        ide_state.subscribe((state) => {
            editor.off('change', onChangeHandler)
            editor.setValue(state)
            editor.on('change', onChangeHandler)
        })
    })

    /**
     * Event handler for the IDE onChange event. Sends the deltas over the websocket.
     * @param event The event caller (IDE).
     */
    function onChangeHandler(event) {
        $wss_ide.sendMessage({...event, user:$username, current_state:editor.getValue()})
        console.log("CHANGE", event)        
    }

    // Disconnect from the IDE websocket when the user leaves the IDE page.
    onDestroy(() => {
        $wss_ide.disconnectWebSocket()
    })


    
</script>

<!-- IDE contents -->
<!-- Div to contain the Brace editor -->
<div id="editor"></div>

<style>
  #editor {
    padding: 1em;
    background-color: black;
    border: 1em solid black;
    height: 40vh;
  }
</style>