<script>
// @ts-nocheck

    import { AceEditor } from "svelte-ace";
    import "brace"
    import "brace/mode/python";
    import "brace/theme/tomorrow_night_bright";
    import "brace/ext/searchbox";
    import "brace/snippets/python"
    import "brace/ext/language_tools"

    let value = 'let x = 10;\nfor (let y in x) {\n\tconsole.log(y);\n}';
    let options = {"fontSize":16, "scrollPastEnd":true, enableBasicAutocompletion: true, enableSnippets: true, enableLiveAutocompletion: true,}
</script>

<div class="editor">
    <AceEditor width='100%' height='300px' lang="python" theme="tomorrow_night_bright" {value} {options}/>
</div>


<style>
    .editor {
        padding: 1em;
        background-color: black;
    }
    
</style>