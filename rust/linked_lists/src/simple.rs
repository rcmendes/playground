use std::fmt;

type Link<T> = Option<Box<Node<T>>>;

#[derive(Debug)]
struct Node<T> {
    value: T,
    next: Link<T>,
}

impl<T> Node<T> {
    fn new(value: T) -> Self {
        Self {
            value: value,
            next: None,
        }
    }
}

#[derive(Debug)]
pub struct SimpleLinkedList<T> {
    head: Link<T>,
}

impl<T> SimpleLinkedList<T> {
    pub fn new() -> Self {
        SimpleLinkedList { head: None }
    }

    pub fn push(&mut self, value: T) {
        let new_node = Box::new(Node::new(value));

        if let Some(ref mut current_head) = self.head {
            let mut current_node = current_head;
            while let Some(ref mut next) = current_node.next {
                current_node = next;
            }

            (*current_node).next = Some(new_node);
        } else {
            self.head = Some(new_node);
        }
    }

    fn pop_alternative(&mut self) -> Option<T> {
        if self.head.is_none() {
            return None;
        }

        let curr_node = &mut self.head;

        Self::pop_last(curr_node)
    }

    fn pop_last(node: &mut Link<T>) -> Option<T> {
        if let Some(current_node) = node {
            if current_node.next.is_some() {
                return Self::pop_last(&mut current_node.next);
            } else {
                return node.take().map(|n| n.value);
            }
        }

        None
    }

    pub fn pop(&mut self) -> Option<T> {
        if self.head.is_none() {
            return None;
        }

        let mut curr_node = &mut self.head;
        while curr_node.as_ref().unwrap().next.is_some() {
            curr_node = &mut curr_node.as_mut().unwrap().next;
        }

        curr_node.take().map(|content| content.value)
    }
}

impl<T> fmt::Display for SimpleLinkedList<T>
where
    T: fmt::Display,
{
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let mut list = String::from("");
        let mut curr_node = &self.head;

        while let Some(ref node) = curr_node {
            list.push_str(&format!("{}", node.value));
            if node.next.is_some() {
                list.push_str(" -> ");
            }
            curr_node = &node.next;
        }
        write!(f, "{}", list)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_push_and_pop() {
        let mut list = SimpleLinkedList::new();

        let item1 = "Item 1".to_owned();
        let item2 = "Item 2".to_owned();
        let item3 = "Item 3".to_owned();

        assert_eq!(list.pop(), None);

        list.push(item1.clone().to_owned());
        list.push(item2.clone().to_owned());
        list.push(item3.clone().to_owned());

        assert_eq!(list.pop(), Some(item3));
        assert_eq!(list.pop(), Some(item2));
        assert_eq!(list.pop(), Some(item1));

        assert_eq!(list.pop(), None);
    }
    #[test]
    fn test_display() {
        let mut list = SimpleLinkedList::new();

        let item1 = "Item 1".to_owned();
        let item2 = "Item 2".to_owned();
        let item3 = "Item 3".to_owned();

        assert_eq!(list.pop(), None);

        list.push(item1.to_owned());
        list.push(item2.to_owned());
        list.push(item3.to_owned());

        assert_eq!(
            format!("{}", list),
            format!("{} -> {} -> {}", item1, item2, item3)
        );
    }
}
