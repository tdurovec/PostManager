import { createRouter, createWebHistory } from 'vue-router'
import PostsView from '../views/PostsView.vue'
import PostView from '../views/PostView.vue'
import PostEditorView from '../views/PostEditorView.vue'
import PostCreateView from '../views/PostCreateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'posts',
      component: PostsView
    },
    {
      path: '/post/:id',
      name: 'post',
      component: PostView,
      props: true,
    },
    {
      path: '/post/:id/edit',
      name: 'post-edit',
      component: PostEditorView,
      props: true,
    },
    {
      path: '/post/create',
      name: 'post-create',
      component: PostCreateView,
    },
  ]
})

export default router
