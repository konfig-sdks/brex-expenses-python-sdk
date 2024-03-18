operation_parameter_map = {
    '/v1/expenses/card/{expense_id}-GET': {
        'parameters': [
            {
                'name': 'expense_id'
            },
            {
                'name': 'expand[]'
            },
        ]
    },
    '/v1/expenses/card-GET': {
        'parameters': [
            {
                'name': 'expand[]'
            },
            {
                'name': 'user_id[]'
            },
            {
                'name': 'parent_expense_id[]'
            },
            {
                'name': 'budget_id[]'
            },
            {
                'name': 'status[]'
            },
            {
                'name': 'payment_status[]'
            },
            {
                'name': 'purchased_at_start'
            },
            {
                'name': 'purchased_at_end'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/expenses/card/{expense_id}-PUT': {
        'parameters': [
            {
                'name': 'expense_id'
            },
            {
                'name': 'memo'
            },
        ]
    },
    '/v1/expenses/card/receipt_match-POST': {
        'parameters': [
            {
                'name': 'receipt_name'
            },
        ]
    },
    '/v1/expenses/card/{expense_id}/receipt_upload-POST': {
        'parameters': [
            {
                'name': 'receipt_name'
            },
            {
                'name': 'expense_id'
            },
        ]
    },
};