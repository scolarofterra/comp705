def test_squared():
	func= lab4.squared_nums
	case1 = [1,2,3]
	expected1 = [1,4,9]
	self.assertEqual(func(case1),expected1)

if __name__ == '__main__':
        try:
                import lab4
                print("lab4.py module found.Testing...")
                unittest.main()
        except ImportError:
                print("Missing lab4.py module")
