<template>
  <div>
    <b-button v-b-modal.mainNewModal
              variant="primary">
      New
    </b-button>
    <b-modal id="mainNewModal"
             ref="modal"
             header-bg-variant="primary"
             header-text-variant="light"
             @ok.prevent="onOK"
             @shown="onShown"
             title="New"
             :ok-title="`Create ${typeName}`"
             size="lg">
      <form @submit.stop.prevent="onSubmit">
        <b-form-group>
          <b-input-group
            class="w-75 align-items-center"
            :prepend="basePath">
            <b-form-input v-model.trim="name"
                          ref="nameInput"
                          type="text"
                          class="flex-fill"
                          pattern="[A-Za-z0-9-_]+"
                          placeholder="Name"
                          title="Name should only match [A-Za-z0-9-_]+"
                          required>
            </b-form-input>
            <b-form-checkbox v-model="isFolder"
                             class="mx-2">
              is Folder
            </b-form-checkbox>
          </b-input-group>
        </b-form-group>
        <b-form-group v-if="!isFolder">
          <b-form-input v-model.trim="url"
                        type="url"
                        placeholder="Link"
                        required>
            </b-form-input>
        </b-form-group>
        <!-- For accepting enter key submit -->
        <b-button ref="submit" type="submit" class="d-none"></b-button>
      </form>
    </b-modal>
</div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'MainNewModal',

  data() {
    return {
      name: '',
      isFolder: false,
      url: '',
    };
  },

  computed: {
    ...mapGetters('main', [
      'makePath',
    ]),
    basePath() {
      return this.makePath('');
    },
    typeName() {
      return this.isFolder ? 'folder' : 'link';
    },
  },

  methods: {
    onShown() {
      this.name = '';
      this.url = '';
      this.$refs.nameInput.focus();
    },
    onOK() {
      this.$refs.submit.click();
    },
    onSubmit() {
      this.$refs.modal.hide();
    },
  },
};
</script>
