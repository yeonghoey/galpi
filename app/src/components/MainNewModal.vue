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
        <b-form-group >
          <b-input-group
            class="w-75 align-items-start"
            :prepend="basePath">
            <div class="flex-fill">
              <b-form-input v-model.trim="name"
                            ref="nameInput"
                            type="text"
                            :state="nameState"
                            placeholder="Name"
                            required>
              </b-form-input>
              <b-form-invalid-feedback>
                {{ nameInvalidFeedback }}
              </b-form-invalid-feedback>
            </div>
            <b-dropdown :text="typeName" variant="success" slot="append">
              <b-dropdown-item @click="isFolder = false">Link</b-dropdown-item>
              <b-dropdown-item @click="isFolder = true">Folder</b-dropdown-item>
            </b-dropdown>
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
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'MainNewModal',

  data() {
    return {
      name: '',
      isFolder: false,
      url: '',
      namePattern: /^[A-Za-z0-9-_]+$/,
    };
  },

  computed: {
    ...mapGetters('main', [
      'makePath',
      'subs',
    ]),
    basePath() {
      return this.makePath('');
    },
    typeName() {
      return this.isFolder ? 'Folder' : 'Link';
    },
    nameState() {
      return (this.nameNotExists && this.namePatternMatches);
    },
    nameNotExists() {
      return !(this.name in this.subs);
    },
    namePatternMatches() {
      return this.namePattern.test(this.name);
    },
    nameInvalidFeedback() {
      if (!this.nameNotExists) {
        return 'Name exists';
      }
      if (!this.namePatternMatches) {
        return 'Name must match [A-Za-z0-9-_]+';
      }
      return '';
    },
  },

  methods: {
    ...mapActions('main', [
      'putSub',
    ]),
    onShown() {
      this.name = '';
      this.url = '';
      this.$refs.nameInput.focus();
    },
    onOK() {
      this.$refs.submit.click();
    },
    onSubmit() {
      if (!this.nameState) {
        return;
      }

      const body = this.isFolder ? {} : { link: this.url };
      const payload = {
        path: this.makePath(this.name),
        name: this.name,
        body,
      };

      this.putSub(payload)
        .finally(() => {
          this.$refs.modal.hide();
        });
    },
  },
};
</script>
