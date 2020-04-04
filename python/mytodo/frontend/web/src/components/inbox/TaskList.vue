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
						<v-form>
							<v-container>
								<v-row>
									<v-col cols="12" sm="6" md="3">
										<v-text-field
											label="Title"
											v-model="editedItem.title"
										></v-text-field>
									</v-col>

									<v-col cols="12" sm="6" md="3">
										<date-picker-modal
											:onSetDate="onUpdateDueDate"
										/>
									</v-col>
								</v-row>
							</v-container>
						</v-form>
					</v-list-item-title>
					<v-list-item-title
						v-else
						v-text="item.title"
					></v-list-item-title>
					<v-list-item-subtitle>
						<v-chip-group column>
							<template v-for="(tag, idxTag) in item.tags">
								<v-chip
									:key="idxTag"
									small
									class="ma-2"
									color="green"
									text-color="white"
									v-if="chip1"
									close
									@click:close="chip1 = false"
									>{{ tag }}</v-chip
								>
							</template>
						</v-chip-group>
						<v-text-field
							v-if="inAddTagMode(index)"
							label="New tag"
							v-model="editedItem.title"
						></v-text-field>
					</v-list-item-subtitle>
				</v-list-item-content>
				<v-list-item-action>
					<v-list-item-action-text
						v-text="item.dueDate"
						v-if="!inEditMode(index)"
					></v-list-item-action-text>
					<v-btn-toggle v-if="inEditMode(index)">
						<v-btn icon small @click="save()">
							<v-icon color="blue">mdi-content-save-edit</v-icon>
						</v-btn>
						<v-btn icon small @click="cancel()">
							<v-icon color="red">mdi-cancel</v-icon>
						</v-btn>
					</v-btn-toggle>
					<v-btn-toggle
						v-else-if="!inEditMode(index) && !inAddTagMode(index)"
					>
						<v-btn icon small @click="addNewTag(index)">
							<v-icon color="green">mdi-tag-plus</v-icon>
						</v-btn>
						<v-btn icon small @click="edit(index)">
							<v-icon color="grey lighten-1">mdi-pencil</v-icon>
						</v-btn>
					</v-btn-toggle>
					<v-btn-toggle v-else-if="inAddTagMode(index)">
						<v-btn icon small @click="saveNewTag()">
							<v-icon color="blue">mdi-content-save-edit</v-icon>
						</v-btn>
						<v-btn icon small @click="cancel()">
							<v-icon color="red">mdi-cancel</v-icon>
						</v-btn>
					</v-btn-toggle>
				</v-list-item-action>
			</v-list-item>
		</template>
	</v-card>
</template>
<script>
import DatePickerModal from "@/components/common/DatePickerModal";

export default {
	components: { DatePickerModal },
	data: () => ({
		addingTag: false,
		editing: false,
		chip1: true,
		selected: undefined,
		editedItem: {
			title: undefined
		},
		items: [
			{
				dueDate: new Date().toISOString().substr(0, 10),
				headline: "Brunch this weekend?",
				title: "Ali Connors",
				subtitle:
					"I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
				tags: ["Tag 1", "Tag 2", "Tag 3"]
			},
			{
				dueDate: new Date().toISOString().substr(0, 10),
				headline: "Summer BBQ",
				title: "me, Scrott, Jennifer",
				subtitle:
					"Wish I could come, but I'm out of town this weekend.",
				tags: ["Tag A", "Tag B"]
			},
			{
				dueDate: new Date().toISOString(),
				headline: "Oui oui",
				title: "Sandra Adams",
				subtitle:
					"Do you have Paris recommendations? Have you ever been?",
				tags: ["Tag X", "Tag Y"]
			},
			{
				dueDate: new Date().toISOString().substr(0, 10),
				headline: "Birthday gift",
				title: "Trevor Hansen",
				subtitle:
					"Have any ideas about what we should get Heidi for her birthday?"
			},
			{
				dueDate: new Date().toISOString().substr(0, 10),
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
			this.items[this.selected].dueDate = this.editedItem.dueDate;
			this.clear();
		},
		cancel: function() {
			console.log("canceling!");
			this.clear();
		},
		edit: function(index) {
			console.log("editing");
			this.selected = index;
			this.editing = true;
			this.editedItem = this.items[index];
		},
		addNewTag: function(index) {
			console.log("adding new tag");
			this.selected = index;
			this.editedItem = this.items[index];
			this.addingTag = true;
		},
		inEditMode: function(index) {
			return this.editing && this.selected === index;
		},
		inAddTagMode: function(index) {
			return this.addingTag && this.selected === index;
		},
		onUpdateDueDate: function(date) {
			console.log(date);
			this.editedItem.dueDate = date;
		},
		clear: function() {
			this.selected = undefined;
			this.editing = false;
			this.addingTag = false;
			this.editedItem = {};
		}
	}
};
</script>
