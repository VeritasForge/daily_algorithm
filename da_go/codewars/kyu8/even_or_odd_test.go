package kyu8

import "testing"

func TestEvenOrOdd(t *testing.T) {
	tests := []struct {
		name   string
		number int
		want   string
	}{
		{name: "2 is even", number: 2, want: "Even"},
		{name: "7 is odd", number: 7, want: "Odd"},
		{name: "0 is even", number: 0, want: "Even"},
		{name: "-1 is odd", number: -1, want: "Odd"},
		{name: "-2 is even", number: -2, want: "Even"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := EvenOrOdd(tt.number); got != tt.want {
				t.Errorf("EvenOrOdd() = %v, want %v", got, tt.want)
			}
		})
	}
}
