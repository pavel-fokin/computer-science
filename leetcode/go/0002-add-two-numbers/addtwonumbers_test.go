package addtwonumbers

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestAddTwoNumbers(t *testing.T) {
	tests := []struct {
		name     string
		l1       *ListNode
		l2       *ListNode
		expected *ListNode
	}{
		{
			"simple",
			&ListNode{1, &ListNode{2, &ListNode{3, nil}}},
			&ListNode{1, &ListNode{2, &ListNode{3, nil}}},
			&ListNode{2, &ListNode{4, &ListNode{6, nil}}},
		},
		{
			"example 1",
			&ListNode{2, &ListNode{4, &ListNode{3, nil}}},
			&ListNode{5, &ListNode{6, &ListNode{4, nil}}},
			&ListNode{7, &ListNode{0, &ListNode{8, nil}}},
		},
		{
			"example 2",
			&ListNode{0, nil},
			&ListNode{0, nil},
			&ListNode{0, nil},
		},
		{
			"example 3",
			&ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, nil}}}}}},
			&ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, nil}}}},
			&ListNode{8, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{0, &ListNode{0, &ListNode{0, &ListNode{1, nil}}}}}}}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := addTwoNumbers(tt.l1, tt.l2)
			fmt.Println("!", result)
			require.Equal(t, tt.expected, result)
		})
	}
}
