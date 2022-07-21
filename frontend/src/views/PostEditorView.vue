<template>

<div>
    <div>
        <input type="text"  v-model="titleInput"/>
        <input type="text"  v-model="bodyInput"/>
    </div>

    <br>
    <button @click="back()">Back</button>
    <button @click="savePost(post.id)">Save</button>
</div>

</template>

<script>

import { API } from '../API.js'

export default ({
    data(){
        return {
            titleInput: "",
            bodyInput: "",
            post: {}
        }
    },

    methods: {
        async getPost(id) {
            try {
                const response = await fetch(
                API.URL+`/api/posts/${id}/`
                );
                this.post = await response.json();
                this.titleInput = this.post.title
                this.bodyInput = this.post.body
            } catch (error) {
                console.log(error);
            }
        },

        async savePost(id) {
            let data = {
                "title":this.titleInput,
                "body":this.bodyInput,
            }
            console.log(data)
            try {
                const response = await fetch(
                API.URL+`/api/posts/${id}/`, {
                    method: 'PUT',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                    }
                );
                let post = await response.json()
                console.log(post)
                this.$router.push({ name: 'post', params: { id: this.post.id }})
            } catch (error) {
                console.log(error);
            }
        },

        back(){
            this.$router.push({ name: 'post', params: { id: this.post.id }})
        },

    },

    created(){
        this.getPost(this.$route.params.id)
    }
})
</script>