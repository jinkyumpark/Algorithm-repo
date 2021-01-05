public class LinkedList {
	private class Node {
		public Node(int value) {
			this.value = value;
		}
		private int value;
		private Node next;
	}
	
	
	private Node first;
	private Node last;
	
	//addFirst
	public void addFirst(int value) {
		Node node = new Node(value);
		
		node.next = this.first;
	}
	//addLast
	public void addlast(int value) {
		var node = new Node(value);
		
		if(first == null) {
			first = last = node;
		}else {
			last.next = node;
			last = node;
		}
	}
	//deleteFirst
	public void deleteFirst() {
		this.first = first.next;
	}
	//deleteLast
	public void deleteLast() {
		//Find the node 1 before last node
		//Set that node to the last node
		
		Node newLast = this.first;
		while(newLast.next != newLast) {
			newLast = newLast.next;
		}
		
		this.last = newLast;
	}
	//contains
	public boolean contains(int value) {
		Node tmp = this.first;
		
		while(tmp.next != tmp) {
			if(tmp.value == value) {
				return true;
			}
			tmp = tmp.next;
		}
		return false;
	}
	//indexOf
	public int indexOf(int value) {
		int index = 0;
		Node tmp = this.first;
		
		while(tmp.next != tmp) {
			if(tmp.value == value) {
				return index;
			}
			tmp = tmp.next;
			index++;
		}
		return -1;
	}
}
 
