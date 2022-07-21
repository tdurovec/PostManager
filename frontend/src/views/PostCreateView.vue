<template>

<div>
    <div>
        <input type="text"  v-model="titleInput"/>
        <input type="text" v-model="bodyInput">
        <input type="number" v-model="userIdInput">

    </div>

    <br>
    <a href="/">Back</a>
    <button @click="savePost()">Save</button>
</div>

</template>

<script>

import { API } from '../API.js'

export default ({
    data(){
        return {
            titleInput: "",
            bodyInput: "",
            userIdInput: "",
        }
    },

    methods: {
        async savePost() {
            let data = {
                'title':this.titleInput,
                'body':this.bodyInput,
                'userId':this.userIdInput,
            }
            try {
                const response = await fetch(
                API.URL+`/api/posts/`, {
                    method:"POST",
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
            });
                this.$router.push({ name: 'posts' })
            } catch (error) {
                console.log(error);
            } 
        }

    },

})
</script>