<template>
  <b-list-group-item class="d-flex justify-content-between"
                     @mouseover="hovering = true"
                     @mouseout="hovering = false">
    <div class="align-self-center mr-4">
      <i class="fa fa-lg"
         :class="icon">
      </i>
    </div>

    <div class="flex-fill d-flex">
      <div class="align-self-center my-1 w-25">
        <b-link :href="absPath">
          <h3 class="d-inline m-0">{{ name }}</h3>
        </b-link>
      </div>
      <div class="w-75 d-flex justify-content-between">
        <div class="align-self-center flex-fill">
          <div v-if="link">
            <div v-if="editing">
              <b-form @submit.stop.prevent="saveEditing"
                      inline>
                <b-input-group class="flex-fill">
                  <b-form-input v-model.trim="editingURL"
                                type="url"
                                placeholder="Link"
                                required>
                  </b-form-input>
                  <b-input-group-append>
                    <b-button type="submit"
                              variant="secondary">
                      Save
                    </b-button>
                  </b-input-group-append>
                </b-input-group>
                <div class="mx-2">
                  or
                  <b-button @click="stopEditing"
                            class="px-0"
                            size="sm"
                            variant="link">
                    Cancel
                  </b-button>
                </div>
              </b-form>
            </div>
            <div v-else > <!-- editing -->
              <b-link :href="link"
                      class="text-secondary">
                {{ link }}
              </b-link>
              <b-button v-if="owner"
                        @click="startEditing"
                        size="sm"
                        variant="muted">
                <i class="fa fa-edit"></i>
              </b-button>
            </div>
          </div>
          <div v-else> <!-- link -->
            <span class="text-secondary">
              {{ count }} {{ countUnit }}
            </span>
          </div>
        </div>

        <div class="align-self-center"
             ref="deleteButtonArea">
          <b-button v-if="owner"
                    v-show="showDelete"
                    @click="deleteItem"
                    class="p-0"
                    variant="link"
                    :disabled="!deletable">
            <i class="fa fa-times text-secondary"></i>
          </b-button>
        </div>
        <b-tooltip v-if="!deletable"
                   :target="() => $refs.deleteButtonArea"
                   placement="left">
          Folder must be empty
        </b-tooltip>
      </div>
    </div>
  </b-list-group-item>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex';
import _ from 'lodash';

export default {
  name: 'MainListGroupItem',

  props: {
    name: {
      type: String,
      required: true,
    },
    body: {
      type: Object,
      required: true,
    },
  },

  data() {
    return {
      hovering: false,
      editing: false,
      editingURL: '',
    };
  },

  computed: {
    ...mapState('main', [
      'owner',
    ]),
    ...mapGetters('main', [
      'base',
      'makePath',
    ]),
    relPath() {
      // ['a', 'b'], 'c' => '/a/b/c'
      return this.makePath(this.name);
    },
    absPath() {
      return `${process.env.APP_BASE_URL}${this.relPath}`;
    },
    link() {
      return _.get(this.body, 'link', '');
    },
    count() {
      const subs = _.get(this.body, 'subs', {});
      return _.size(subs);
    },
    countUnit() {
      return this.count < 2 ? 'item' : 'items';
    },
    isFolder() {
      return this.link === '';
    },
    icon() {
      return this.isFolder ? 'fa-folder-o' : 'fa-link';
    },
    showDelete() {
      return this.hovering && !this.editing;
    },
    deletable() {
      return (!this.isFolder ||
              (this.isFolder && this.count === 0));
    },
  },

  methods: {
    ...mapActions('main', [
      'putSub',
      'deleteSub',
    ]),
    startEditing() {
      this.editing = true;
      this.editingURL = this.link;
    },
    stopEditing() {
      this.editing = false;
    },
    saveEditing() {
      const body = { link: this.editingURL };
      const payload = {
        path: this.relPath,
        name: this.name,
        body,
      };
      this.putSub(payload)
        .finally(() => {
          this.editing = false;
        });
    },
    deleteItem() {
      const payload = {
        path: this.relPath,
        name: this.name,
      };
      this.deleteSub(payload);
    },
  },
};
</script>
