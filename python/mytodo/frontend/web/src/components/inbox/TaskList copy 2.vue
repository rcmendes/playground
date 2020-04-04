<template>
  <v-card max-width="500" class="mx-auto">
    <v-toolbar color="primary" dark>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Inbox</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-checkbox-marked-circle</v-icon>
      </v-btn>
    </v-toolbar>

    <template v-for="(item, index) in items">
      <v-list-item two-line :key="item.title">
        <v-list-item-content>
          <v-list-item-title v-if="inEditMode(index)">
            <v-text-field label="Title" v-model="editedItem.title"></v-text-field>
          </v-list-item-title>
          <v-list-item-title v-else v-text="item.title"></v-list-item-title>
          <v-list-item-subtitle>
            <v-chip-group column>
              <v-chip x-small class="ma-2" color="primary">Primary</v-chip>
              <v-chip x-small class="ma-2" color="secondary">Secondary</v-chip>
              <v-chip x-small class="ma-2" color="red" text-color="white">Red Chip</v-chip>
              <v-chip x-small class="ma-2" color="green" text-color="white">Green Chip</v-chip>
            </v-chip-group>
          </v-list-item-subtitle>
        </v-list-item-content>
        <v-list-item-action>
          <v-list-item-action-text v-if="inEditMode(index)">
            <v-text-field label="Due date" v-model="editedItem.dueDate"></v-text-field>
          </v-list-item-action-text>
          <v-list-item-action-text v-else v-text="item.action"></v-list-item-action-text>
          <v-btn-toggle>
            <v-btn icon v-if="inEditMode(index)" @click="save()">
              <v-icon color="blue">mdi-content-save-edit</v-icon>
            </v-btn>
            <v-btn icon v-if="inEditMode(index)" @click="cancel()">
              <v-icon color="blue">mdi-cancel</v-icon>
            </v-btn>
            <v-btn icon v-else @click="edit(index)">
              <v-icon color="grey lighten-1">mdi-pencil</v-icon>
            </v-btn>
          </v-btn-toggle>
        </v-list-item-action>
      </v-list-item>
    </template>
  </v-card>
</template>
<script>
export default {
  data: () => ({
    selected: undefined,
    editedItem: {
      title: undefined
    },
    items: [
      {
        action: "05/03/2020 10:30am",
        headline: "Brunch this weekend?",
        title: "Ali Connors",
        subtitle:
          "I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
      },
      {
        action: "2 hr",
        headline: "Summer BBQ",
        title: "me, Scrott, Jennifer",
        subtitle: "Wish I could come, but I'm out of town this weekend."
      },
      {
        action: "6 hr",
        headline: "Oui oui",
        title: "Sandra Adams",
        subtitle: "Do you have Paris recommendations? Have you ever been?"
      },
      {
        action: "12 hr",
        headline: "Birthday gift",
        title: "Trevor Hansen",
        subtitle:
          "Have any ideas about what we should get Heidi for her birthday?"
      },
      {
        action: "18hr",
        headline: "Recipe to try",
        title: "Britta Holt",
        subtitle:
          "We should eat this: Grate, Squash, Corn, and tomatillo Tacos."
      }
    ]
  }),
  methods: {
    save: function() {
      console.log("saving!");
      this.items[this.selected].title = this.editedItem.title;
      this.items[this.selected].action = this.editedItem.dueDate;
      this.selected = undefined;
      this.editedItem = {};
    },
    cancel: function() {
      console.log("canceling!");
      this.selected = undefined;
      this.editedItem = {};
    },
    edit: function(index) {
      console.log(index);
      this.selected = index;
      this.editedItem.title = this.items[index].title;
      this.editedItem.dueDate = this.items[index].action;
    },
    inEditMode: function(index) {
      return parseInt(this.selected) === index;
    }
  }
};
</script>
