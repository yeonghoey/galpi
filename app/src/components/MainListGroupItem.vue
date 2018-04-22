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
              <b-form @submit.prevent="saveEditing"
                      inline>
                <b-input-group class="flex-fill">
                  <b-form-input type="url"
                                placeholder="Link"
                                v-model.trim="editingURI">
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

        <div class="align-self-center">
          <b-button v-show="deletable"
                    @click="deleteItem"
                    class="p-0"
                    variant="link">
            <i class="fa fa-times text-secondary"></i>
          </b-button>
        </div>
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
      editingURI: '',
    };
  },

  computed: {
    ...mapState('main', [
      'owner',
    ]),
    ...mapGetters('main', [
      'base',
    ]),
    relPath() {
      // ['a', 'b'], 'c' => '/a/b/c'
      const segs = _.concat([''], this.base, this.name);
      return _.join(segs, '/');
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
    deletable() {
      return this.hovering && !this.editing;
    },
  },

  methods: {
    ...mapActions('main', [
      'putSub',
      'deleteSub',
    ]),
    startEditing() {
      this.editing = true;
      this.editingURI = this.link;
    },
    stopEditing() {
      this.editing = false;
    },
    saveEditing() {
      const body = { link: this.editingURI };
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
