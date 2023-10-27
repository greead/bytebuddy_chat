<script>
    import {user} from "./store.js"
    // var email;
    // var password;
    async function handleForm(event){
        event.preventDefault();
        // user.set({
        //     email,
        //     password});
        console.log($user)
        try{
            
            const reponse = await fetch('http://127.0.0.1:8000/api/signup', {
                method: 'POST',
                headers:{
                    'Content-Type': 'application/json',
                },
                // something is wrong with user- it has 
                body: JSON.stringify($user),
            });
            
            if(reponse.ok){
                console.log('Sign up succesfully');
            }
            else{
                const error = await reponse.json();
                console.error(error.message);
            }
        }
        catch(error){
            console.error(error);
        }
    }
</script>

<h1>ByteBuddy Signup</h1>
<form on:submit={handleForm}>
    <lable for="email">Email: </lable>
    <input bind:value={$user.email} type="text" id="email" name="email" style="input_item"><br>
    <lable for="pw">Password: </lable>
    <input bind:value={$user.password} type="password" id="pw" name="pw"><br>
    <lable for="cpw">Confirm Password: </lable>
    <input type="password" id="cpw" name="cpw"><br>
    <input type="submit" id="button" value="Sign Up">
</form>

<style>
    form{
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    input{
        width:20em;
        
    }

    #button{
        width:10em;
    }

</style>