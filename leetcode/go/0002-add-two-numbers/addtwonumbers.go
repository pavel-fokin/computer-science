package addtwonumbers

import (
	"fmt"
	"strings"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func (l *ListNode) String() string {
	var sb strings.Builder

	for l != nil {
		sb.WriteString(fmt.Sprintf("%d ", l.Val))
		l = l.Next
	}
	sb.WriteString("nil")

	return sb.String()
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := &ListNode{}
	resultRoot := result
	memory := 0

	for (l1 != nil) || (l2 != nil) {
		val := l1.Val + l2.Val + memory
		if val > 9 {
			memory = 1
			result.Val = 10 - val
		} else {
			result.Val = val
		}
		if (l1.Next != nil) || (l2.Next != nil) {
			result.Next = &ListNode{}
			result = result.Next
		}
		if l1.Next != nil {
			l1 = l1.Next
		}
		if l2.Next != nil {
			l2 = l2.Next
		}
	}

	return resultRoot
}
