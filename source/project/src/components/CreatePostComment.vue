<template>
  <div class="q-pa-md q-gutter-sm">
    <q-select
      color="white"
      dark
      filled
      v-model="NewPost.branche"
      :options="branches"
      label="Choissisez une branche"
    />
    <q-input
      outlined
      dark
      v-model="NewPost.title"
      color="white"
      text-color="white"
      label-color="white"
      label="Résumez votre problème"
    />
    <p class="text-white">Décrivez votre problème:</p>
    <q-editor
      dark
      v-model="NewPost.description"
      :dense="$q.screen.lt.md"
      :toolbar="[
        [
          {
            label: $q.lang.editor.align,
            icon: $q.iconSet.editor.align,
            fixedLabel: true,
            list: 'only-icons',
            options: ['left', 'center', 'right', 'justify'],
          },
        ],
        ['bold', 'italic', 'strike', 'underline', 'subscript', 'superscript'],
        ['token', 'hr', 'link', 'custom_btn'],
        ['fullscreen'],
        [
          {
            label: $q.lang.editor.formatting,
            icon: $q.iconSet.editor.formatting,
            list: 'no-icons',
            options: ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'code'],
          },
          {
            label: $q.lang.editor.fontSize,
            icon: $q.iconSet.editor.fontSize,
            fixedLabel: true,
            fixedIcon: true,
            list: 'no-icons',
            options: [
              'size-1',
              'size-2',
              'size-3',
              'size-4',
              'size-5',
              'size-6',
              'size-7',
            ],
          },
          {
            label: $q.lang.editor.defaultFont,
            icon: $q.iconSet.editor.font,
            fixedIcon: true,
            list: 'no-icons',
            options: [
              'default_font',
              'arial',
              'arial_black',
              'comic_sans',
              'courier_new',
              'impact',
              'lucida_grande',
              'times_new_roman',
              'verdana',
            ],
          },
        ],
        ['quote', 'unordered', 'ordered', 'outdent', 'indent'],
        ['undo', 'redo'],
      ]"
      :fonts="{
        arial: 'Arial',
        arial_black: 'Arial Black',
        comic_sans: 'Comic Sans MS',
        courier_new: 'Courier New',
        impact: 'Impact',
        lucida_grande: 'Lucida Grande',
        times_new_roman: 'Times New Roman',
        verdana: 'Verdana',
      }"
    />
    <div class="q-gutter-sm row items-start">
      <q-btn
        color="secondary"
        icon="mail"
        icon-right="send"
        label="Envoyez"
        @click="
          isAvailable(NewPost);
          $emit(`finished`);
        "
      />
      <div v-if="CommentStore.isAvailableVar == false">
        <h7 class="text-white">Il manque au moins une entrée</h7>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useUserStore } from 'stores/user.js';
import { useCommentStore } from 'stores/comment.js';

//setting of variables/objects

//allows you to access the store
const CommentStore = useCommentStore();

//allows you to access the store
const UserStore = useUserStore();

//retrieve the list of branches
const branches = JSON.parse(localStorage.getItem('Branches'));

//allows you to create the object of the new publication/new comment
const NewPost = reactive({
  title: '',
  branche: '',
  description: '',
  name: '',
  id: '',
  date: '',
  comment: [],
});

// setting of functions

//allows you to check if all the fields are filled in
//displays a message indicating that not all fields are filled in
function isAvailable(NewPost) {
  CommentStore.isAvailableVar = false;
  if (
    NewPost.title !== '' &&
    NewPost.branche !== '' &&
    NewPost.description !== ''
  ) {
    CommentStore.isAvailableVar = true;
    CommentStore.addComment(
      'post',
      NewPost.id,
      NewPost,
      UserStore.Profile.name,
      UserStore.Profile.mail,
      UserStore.Profile.password,
      UserStore.pp_profile,
      'localStorage'
    );
    resetNewPost();
  }
}

//allows you to reset the fields
function resetNewPost() {
  NewPost.title = '';
  NewPost.branche = '';
  NewPost.description = '';
}
</script>
