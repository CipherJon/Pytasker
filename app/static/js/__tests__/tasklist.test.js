import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import TaskList from '../components/tasklist';

test('renders Task List heading', () => {
  render(<TaskList />);
  expect(screen.getByText('Task List')).toBeInTheDocument();
});