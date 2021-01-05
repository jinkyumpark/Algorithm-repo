package programmingWithMosh;

public class LinkedList {
	private Node first;
	private Node last;
	
	//addFirst
	public void addFirst(int value) {
		Node node = new Node();
		
		node.setValue(value);
		node.setNext(this.first);
	}
	//addLast
	public void addlast(int value) {
		Node node = new Node();
		node.setValue(value);
		
		last.setNext(node);
	}
	//deleteFirst
	public void deleteFirst() {
		this.first = first.getNext();
	}
	//deleteLast
	public void deleteLast() {
		//Find the node 1 before last node
		//Set that node to the last node
		
		
	}
	//contains
	//indexOf
	
}
 
