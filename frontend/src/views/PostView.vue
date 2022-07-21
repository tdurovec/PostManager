<template>

<div>
    <div>
        <h2>{{ post.title }}</h2>
        <p>{{ post.body }}</p>
        <strong>userId: {{ post.userId }}</strong>
    </div>

    <br>
    <button @click="back()">Back</button>
    <button @click="delete_post(post.id)">Delete</button>
    <button @click="edit_post(post.id)">Edit</button>
</div>
  
</template>

<script>

import { API } from '../API.js'

export default ({
    data(){
        return {
            post: {}
        }
    },

    methods: {
        async getPost(id) {
            try {
                const response = await fetch(
                API.URL+`/api/posts/${id}/`
                );
                // JSON responses are automatically parsed.
                this.post = await response.json();
            } catch (error) {
                console.log(error);
            }
        },

        async delete_post(id){
            if (window.confirm('Really delete this post?'))
            {
                let delete_response = await fetch(API.URL+`/api/posts/${id}/`,{ method: 'DELETE',})
                this.back()
            }

        },

        edit_post(id){
            this.$router.push({ name: 'post-edit' })
        },

        back(){
            this.$router.push({ name: 'posts' })
        },


    },

    created(){
        this.getPost(this.$route.params.id)
    }
})
</script>
