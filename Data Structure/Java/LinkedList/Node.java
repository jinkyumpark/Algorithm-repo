public class Node {
	private int value;
	private Node next;
	
	//getter
	public int getValue() {
		return this.value;
	}
	
	public Node getNext() {
		return this.next;
	}
	
	//setter
	public void setValue(int value) {
		this.value = value;
	}
	
	public void setNext(Node node) {
		this.next = node;
	}
	
}
