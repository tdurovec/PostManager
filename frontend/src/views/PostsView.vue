<template>
<div>
    <br>
    <br>
    <div v-for="post in posts" v-bind:key="post.id">
         <router-link :to="{ name: 'post', params: { id: post.id }}">{{post.title}}</router-link>
        <p>{{ post.body }}</p>
        <br>
    </div>
</div>

</template>

<script>
import { API } from '../API.js'

export default {
    data(){
        return {
            posts: []
        }
    },

    methods: {
        async getPosts() {
            try {
                const response = await fetch(
                API.URL+"/api/posts/"
                );
                // JSON responses are automatically parsed.
                this.posts = await response.json();
            } catch (error) {
                console.log(error);
            }
        }
    },

    created(){
        this.getPosts()
    }


}
</script>
